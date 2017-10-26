#!/usr/bin/env python

import functools
import operator

import memory_profiler


class MemoryUsageException(Exception):
    pass


def _assert_wrapper(fn, op=operator.not_, failure_message="Max usage {}"):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        (mem_usage, retval) = memory_profiler.memory_usage(
            (fn, args, kwargs),
            max_usage=True,
            retval=True
        )

        max_usage = round(mem_usage[0], 2)

        if not op(max_usage):
            raise MemoryUsageException(failure_message.format(max_usage))

        return retval

    return wrapper


def _reverse_args(fn):
    """We're frequently reversing the arguments of operators because the
    value we're planning to compare against is the first argument which makes
    partial application difficult.
    """
    def reverse(*args, **kwargs):
        return fn(*args[::-1], **kwargs)

    return reverse


assert_mb = _assert_wrapper


def assert_lt_mb(mb):
    wrapper = functools.partial(
        _assert_wrapper,
        op=functools.partial(_reverse_args(operator.lt), mb),
        failure_message="Max usage {}Mb >= {}Mb".format("{}", mb)
    )

    return wrapper


def assert_le_mb(mb):
    wrapper = functools.partial(
        _assert_wrapper,
        op=functools.partial(_reverse_args(operator.le), mb),
        failure_message="Max usage {}Mb > {}Mb".format("{}", mb)
    )

    return wrapper


def assert_eq_mb(mb):
    wrapper = functools.partial(
        _assert_wrapper,
        op=functools.partial(operator.eq, mb),
        failure_message="Usage {}Mb != {}Mb".format("{}", mb)
    )

    return wrapper


def assert_ne_mb(mb):
    wrapper = functools.partial(
        _assert_wrapper,
        op=functools.partial(operator.ne, mb),
        failure_message="Usage {}Mb == {}Mb".format("{}", mb)
    )

    return wrapper


def assert_ge_mb(mb):
    wrapper = functools.partial(
        _assert_wrapper,
        op=functools.partial(_reverse_args(operator.ge), mb),
        failure_message="Min usage {}Mb < {}Mb".format("{}", mb)
    )

    return wrapper


def assert_gt_mb(mb):
    wrapper = functools.partial(
        _assert_wrapper,
        op=functools.partial(_reverse_args(operator.gt), mb),
        failure_message="Min usage {}Mb <= {}Mb".format("{}", mb)
    )

    return wrapper
