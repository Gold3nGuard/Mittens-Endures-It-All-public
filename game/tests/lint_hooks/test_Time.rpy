init -98 python:

    @test_case
    def test_advanceTime():

        time = Time(hour=17, minute=30)
        time.advanceTime()


        expected = time
        actual = Time(17, 32)
        assert expected == actual, f"Time advanced incorrectly!\n Expected = {expected} \n Actual   = {actual}"
