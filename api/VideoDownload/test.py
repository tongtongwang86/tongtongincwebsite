import yt_dlp




class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


# ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)

def replace_after_second_last_dot_with_mov(input_string):
    # Split the string based on dots
    parts = input_string.split('.')

    # If there are at least two dots, join the parts up to the second last dot
    if len(parts) >= 2:
        result = '.'.join(parts[:-2])  # Use [:-2] to exclude the last two parts (extension and file name)
    else:
        # If there are fewer than two dots, return the original string
        result = input_string

    # Add ".mov" to the result
    result += ".mov"

    return result






    
def my_hook(d):

    
    if d['status'] == 'downloading':
        total_bytes_estimate = d.get('total_bytes_estimate', None)
        downloaded_bytes = d.get('downloaded_bytes', None)
        if total_bytes_estimate is not None:
            if downloaded_bytes is not None:
                print((downloaded_bytes/total_bytes_estimate)*100)
     

    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')
        fn = d['filename']
        res = replace_after_second_last_dot_with_mov (fn)
        print (res)
        
            
    
        
        
#        print (len(filesname))
            
    




def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + separated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }


def downloadthevid(URLS):


   
    ydl_opts = {
        'format': format_selector,
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mov'}],
         'logger': MyLogger(),
        'progress_hooks': [my_hook],
#        'forceprint': {'video': ['filename']},
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #    print(ydl_opts)
        ydl.download(URLS)
        

downloadthevid('url')


