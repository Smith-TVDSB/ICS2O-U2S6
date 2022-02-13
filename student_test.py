import pytest
import student 

def test_one(capsys):
    student.cowabungaFunction(1)
    out, err = capsys.readouterr()
    assert "cowabunga\n" == out.lower(), "make sure you're using the function properly not just the main"

def test_two(capsys):
    student.cowabungaFunction(2)
    out, err = capsys.readouterr()
    assert out.lower() == "cowabungacowabunga\n"

def test_eight(capsys):
    student.cowabungaFunction(8)
    out, err = capsys.readouterr()
    assert out.lower() == "cowabungacowabungacowabungacowabungacowabungacowabungacowabungacowabunga\n"

def test_many(capsys):
    for i in range(2,100):
        student.cowabungaFunction(i)
        out, err = capsys.readouterr()
        assert out.lower() == ("cowabunga"*i)+"\n", "Didn't work for"+str(i)

