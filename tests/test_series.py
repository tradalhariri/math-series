from math_series.series import fibonacci,lucas,sumSeries


def test_fibonacci():
    assert 0 == fibonacci(0)
    assert 1 == fibonacci(1)
    assert 5 == fibonacci(5)
    assert 8 == fibonacci(6)
    assert 13 == fibonacci(7)

def test_lucas():
    assert 2 == lucas(0)
    assert 1 == lucas(1)
    assert 3 == lucas(2)
    assert 4 == lucas(3)
    assert 7 == lucas(4)
    assert 11 == lucas(5)
    assert 18 == lucas(6)
def test_sumSeries():

    assert 0 == sumSeries(0)
    assert 1 == sumSeries(1)
    assert 5 == sumSeries(5)
    assert 8 == sumSeries(6)

    assert 7 == sumSeries(4,2,1)
    assert 11 == sumSeries(5,2,1)
    assert 18 == sumSeries(6,2,1)


    assert 50 == sumSeries(4,10,10)

