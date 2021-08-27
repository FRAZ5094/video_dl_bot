# youtube-dl video_url --max-filesize 8m -o "youtube-dl_vid.%(ext)s"
# youtube-dl --list-extractors | grep -i search

import subprocess


def youtube_dl(url):
    dl_string = "youtube-dl {url} --max-filesize 8m -o ~/github/video_dl_bot/youtube-dl_vid.%(ext)s".format(
        url=url
    )
    command = dl_string.split(" ")
    print(command)

    out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    output = stdout.decode("utf-8")
    return output


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=TVg1gb9kMmM"
    output = youtube_dl(url)
    print(output)
