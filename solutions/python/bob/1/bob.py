def response(hey_bob):
    msg = hey_bob.strip()

    is_silence = msg == ""
    is_question = msg.endswith("?")
    is_shouting = msg.isupper() and any(ch.isalpha() for ch in msg)

    if is_silence:
        return "Fine. Be that way!"
    elif is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_shouting:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
