import emojis

def converter_text_to_emojis(text):
		switcher = {
			list: text,
			str: [text]
		}
		text = switcher.get(type(text), TypeError)
		emoret = list()
		for emotxt in text:
			tmp = emojis.encode(emotxt)
			emoret.append(tmp)
		return emoret