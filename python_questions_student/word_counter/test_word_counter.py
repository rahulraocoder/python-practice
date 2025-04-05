from word_counter import analyze_text

def test_basic_text():
    text = "Hello world hello python"
    result = analyze_text(text)
    assert result['total_words'] == 4
    assert result['unique_words'] == 3
    assert ('hello', 2) in result['most_common']
    assert abs(result['avg_length'] - 4.75) < 0.01

def test_empty_text():
    result = analyze_text("")
    assert result['total_words'] == 0
    assert result['unique_words'] == 0
    assert result['most_common'] == []
    assert result['avg_length'] == 0

def test_punctuation():
    text = "Hello, world! Hello? Python..."
    result = analyze_text(text)
    assert result['total_words'] == 4
    assert ('hello', 2) in result['most_common']

def test_case_insensitivity():
    text = "Hello hello HELLO"
    result = analyze_text(text)
    assert result['total_words'] == 3
    assert result['unique_words'] == 1
    assert ('hello', 3) in result['most_common']
