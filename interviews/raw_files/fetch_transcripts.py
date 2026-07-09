from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = {
    "삼일PwC": "y0SsTKDt8tQ",
    "카카오페이증권": "aBuoojGjyf4",
    "메디테라피": "1KwyhyBo0Rs",
    "마이리얼트립": "qGMVO0tjjGE",
    "무신사": "OLAWeIuiD5Y",
    "채널톡": "5iRf37Z8Wd4"
}

output_dir = "/Users/gabrieljang/Documents/AX Hackerton"

api = YouTubeTranscriptApi()

for company, video_id in videos.items():
    try:
        # Fetch Korean transcript
        transcript_list = api.list(video_id)
        # Try to find a korean transcript (either manual or auto-generated)
        transcript = transcript_list.find_transcript(['ko']).fetch()
        
        md_content = f"# {company} 기업 인터뷰 스크립트\n\n"
        md_content += f"**영상 링크:** [https://www.youtube.com/watch?v={video_id}](https://www.youtube.com/watch?v={video_id})\n\n"
        
        for item in transcript:
            text = item.text.replace('\n', ' ')
            md_content += f"- {text}\n"
            
        file_path = os.path.join(output_dir, f"{company}_인터뷰_스크립트.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Successfully saved transcript for {company}")
        
    except Exception as e:
        print(f"Failed to get transcript for {company} ({video_id}): {e}")
