def test_zero_weight_returns_maximum_flight_time():
    from flight_calculator import calculate_flight_time
    assert calculate_flight_time(0) == 180


def test_typical_weight_uses_expected_formula():
    from flight_calculator import calculate_flight_time
    assert calculate_flight_time(500) == 130
    assert calculate_flight_time(1000) == 80


def test_zero_flight_time_at_formula_cutoff():
    from flight_calculator import calculate_flight_time
    assert calculate_flight_time(1800) == 0


def test_flight_time_cannot_be_negative_above_cutoff():
    from flight_calculator import calculate_flight_time
    assert calculate_flight_time(2500) == 0
    assert calculate_flight_time(10000) == 0


def test_negative_weight_raises_value_error():
    import pytest
    from flight_calculator import calculate_flight_time
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_flight_time(-1)


def test_large_negative_weight_raises_value_error():
    import pytest
    from flight_calculator import calculate_flight_time
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_flight_time(-1000)

def test_flight_time_table_with_zero_maximum_weight():
    from flight_calculator import flight_time_table

    assert flight_time_table(0, 100) == [(0, 180)]


def test_flight_time_table_returns_weights_at_step_intervals():
    from flight_calculator import flight_time_table

    assert flight_time_table(1000, 250) == [
        (0, 180),
        (250, 155.0),
        (500, 130.0),
        (750, 105.0),
        (1000, 80.0),
    ]


def test_flight_time_table_includes_aligned_maximum_weight():
    from flight_calculator import flight_time_table

    table = flight_time_table(600, 200)

    assert table[-1] == (600, 120.0)
    assert len(table) == 4


def test_flight_time_table_excludes_unreachable_maximum_weight():
    from flight_calculator import flight_time_table

    assert flight_time_table(650, 200) == [
        (0, 180),
        (200, 160.0),
        (400, 140.0),
        (600, 120.0),
    ]


def test_flight_time_table_clamps_flight_time_to_zero():
    from flight_calculator import flight_time_table

    table = flight_time_table(4000, 1000)

    assert table == [
        (0, 180),
        (1000, 80.0),
        (2000, 0),
        (3000, 0),
        (4000, 0),
    ]


def test_flight_time_table_rejects_negative_maximum_weight():
    import pytest
    from flight_calculator import flight_time_table

    with pytest.raises(
        ValueError,
        match="Max weight must be non-negative and step must be positive",
    ):
        flight_time_table(-1, 100)


def test_flight_time_table_rejects_zero_step():
    import pytest
    from flight_calculator import flight_time_table

    with pytest.raises(
        ValueError,
        match="Max weight must be non-negative and step must be positive",
    ):
        flight_time_table(1000, 0)


def test_flight_time_table_rejects_negative_step():
    import pytest
    from flight_calculator import flight_time_table

    with pytest.raises(
        ValueError,
        match="Max weight must be non-negative and step must be positive",
    ):
        flight_time_table(1000, -100)


def test_flight_time_table_calls_calculate_flight_time_for_each_weight(
    monkeypatch,
):
    import flight_calculator

    calls = []

    def fake_calculate_flight_time(weight):
        calls.append(weight)
        return weight + 1

    monkeypatch.setattr(
        flight_calculator,
        "calculate_flight_time",
        fake_calculate_flight_time,
    )

    result = flight_calculator.flight_time_table(600, 200)

    assert calls == [0, 200, 400, 600]
    assert result == [
        (0, 1),
        (200, 201),
        (400, 401),
        (600, 601),
    ]