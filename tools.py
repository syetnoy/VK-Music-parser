from csv import writer as wr
from time import strftime, localtime


def get_now() -> str:
	return strftime('%d.%m.%Y %H.%M', localtime())


def write_txt(file_name: str, mode_job: str, now: str, count: int, text: str) -> None:
	with open(f'{file_name} {now}.txt', mode=mode_job, encoding='utf-8') as file:
		file.write(f'{count}. {text}\n')


def write_csv(file_name: str, mode_job: str, now: str, count: int, title: str, artist: str) -> None:
	with open(f'{file_name} {now}.csv', mode=mode_job, newline='', encoding='utf-8') as file:
		writer = wr(file)
		writer.writerow([count, title, artist])
