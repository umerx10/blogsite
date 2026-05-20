from groq import Groq
from django.conf import settings



def generate_summary(text):
     
     try:

        client=Groq(api_key=settings.GROQ_API_KEY)


        response=client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[
                {
                    "role":"user",
                    "content":(
                        "Summarize the following blogpost\n"
                        f"Post Content: \n{text}"
                    )
                }
            ],

            max_tokens=200,
            temperature=0.4,

        )

        summary=response.choices[0].message.content
        return summary
     
     except Exception as e:
         return f"Sorry! Summary cant be generated ({str(e)})"
