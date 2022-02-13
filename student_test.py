import pytest
import student 

def test_one():
    student.cowabungaFunction(1)
    out, err = capsys.readouterr()
    assert out.lower() == "cowabunga"

def test_two():
    student.cowabungaFunction(2)
    out, err = capsys.readouterr()
    assert out.lower() == "cowabungacowabunga"

def test_eight():
    student.cowabungaFunction(8)
    out, err = capsys.readouterr()
    assert out.lower() == "cowabungacowabungacowabungacowabungacowabungacowabungacowabungacowabunga"




#Standard test output ONLY (no input)
#No need for the if __name__ condition in the main code, but might as well when done so students get used to it.
"""def test_hello(capsys):
    import hello
    out,err = capsys.readouterr()
    assert out == "Hello world!\n" or "bye" in out, "Should read 'Hello world!' "
"""

# Tests multiple values one at a time:

# def test_higher():
#     for i in [19, 91, 20, 24, 54, 33, 18]:
#         input_values=[str(i)]
#         output=[]

#         def mock_input(s=None):
#             if s is not None:
#                 output.append(s)
#                 return input_values.pop(0)
#             else:
#                 output.append("")
#                 return input_values.pop(0)
        
#         student.input = mock_input
#         student.print = lambda s : output.append(s)

#         student.main()

#         assert "true" in output[1].lower()
