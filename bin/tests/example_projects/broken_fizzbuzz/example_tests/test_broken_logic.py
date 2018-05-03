import os, sys
from broken_fizzbuzz_context import *

def test_broken_fizz():
    return Expect(Fizzbuzz.run(3)).to_equal('Fizz')

def test_broken_buzz():
    return Expect(Fizzbuzz.run(5)).to_equal('Buzz')

def test_broken_fizzbuzz():
    return Expect(Fizzbuzz.run(15)).to_equal('Fizzbuzz')

def test_broken_number():
    Expect(Fizzbuzz.run(1)).to_equal(1)
