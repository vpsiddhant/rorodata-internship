import almostEqual
import pytest


@pytest.mark.parametrize("first,second,resultva",
			[
				("python","pearl",False),
				("pearl","perl",True),
				("python","jython",True),
				("man","woman",False)
			]
			)
def test_almost_equal(first,second,resultva):
	result = almostEqual.almost_equal(first,second)
	assert result == resultva



#test_almost_equal("raj","taj",True)

