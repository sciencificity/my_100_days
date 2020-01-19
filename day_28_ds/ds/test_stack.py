from stack import Stack
# day_28_ds.ds.stack

import pytest

@pytest.fixture
def stack():
    # PyTest fixtures, which are a great way to provide a fixed baseline
    # upon which tests can reliably and repeatedly executed.
    return Stack()

def test_constructor():
    s = Stack()
    assert isinstance(s, Stack)
    # our Stack is a datastructure and we want it to contain data
    # so here we test if len of stack we just initialised is 0
    assert len(s) == 0

def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2

def test_pop(stack):
    stack.push('hello')
    stack.push('world')
    assert stack.pop() == 'world'
    assert stack.pop() == 'hello'
    assert stack.pop() is None