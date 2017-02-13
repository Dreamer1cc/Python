def median(numbers):
	srt_numb = sorted(numbers)
	len_srt_numb = len(srt_numb)
	if len_srt_numb == 1:
		return srt_numb[0]
	elif len_srt_numb % 2 == 0:
		med = ((srt_numb[len_srt_numb / 2] + srt_numb[(len_srt_numb / 2 - 1)]) / 2.0)
		return med
	elif len_srt_numb % 2 != 0:
		med = srt_numb[len_srt_numb / 2]
		return med


median([5, 4, 2])