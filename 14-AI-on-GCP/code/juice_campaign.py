import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


def generate():
    vertexai.init(project="YOUR_GCP_PROJECT", location="europe-west4")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[textsi_1]
    )
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

text1 = """# **Client**: **BuzzJuice**

## Brand Information:
* Buzzjuice is the only energy drink with all-organic ingredients.
* BuzzJuice has created an energy-boosting formula incorporating non-traditional ingredients, such as Ashwagandha, Lion\'s Mane, L-Theanine, and Yerba mate. The formula produces functional benefits that go beyond just an initial energy boost. The ingredients have a wide-ranging set of additional benefits, such as improved focus, mood enhancement, and immune support.
* BuzzJuice comes in 3 unique flavors: Hibiscus Lime, Tamarind Grape, and Lavender Berry.
* The packaging consists of only recycled materials and is biodegradable, resulting in zero net-waste.
* The target audience is anyone who could benefit from an energy boost and functional focus without sacrificing their health.

## Campaign Goals:

* Target Audience: ages 14-29, from high-school students all the way to young professionals, and fitness enthusiasts. The BuzzJuice drinker is always on the go, while valuing health, and wellness. They are both health- and trend conscious.
* Brand values: Innovation, sustainability, and transparency.
* Brand voice and tone: Energetic, motivating, edgy. The tone must resonate with the youthful target audience. Use dynamic language that inspires action. Avoid being overly trendy, and remain authentic.

## Deliverables:

* Create a concise tagline that communicates the brand\'s vibe. It should be a short sentence or phrase.

* Create a character named Dr. Buzz to be featured in TV and online ads. He should be goofy, and eccentric. Think Doc Brown from the movie Back to the Future. Provide detailed information about wardrobe, hair-and make-up, and voice.

* Create an Instagram profile for Dr. Buzz. Provide concepts for the first 2 posts.
* Each post must be goofy, and eccentric, like Dr. Buzz himself.

* Create 2 TikTok pitches. One should feature Dr. Buzz creating a unique TikTok dance. He must be terrible at dancing, but his energy must be infectious.
* Each post must be goofy, and eccentric, like Dr. Buzz himself."""
textsi_1 = """You are an expert advertising creative director who specializes in generating exciting campaigns that tend to go viral. Your specialties are the beverage category and reaching the Gen-Z market. You will be given specific instructions for each campaign. Your instructions will contain a client\\\'s name, relevant information, and deliverables. If your instructions are missing any of this data, ask the user to provide it. Be courteous and professional.

## General Rules
* Your overarching objective is to create brand awareness engagement.
* You understand the Target Audience to be the demographic you are targeting with brand material.
* You understand Brand Values as parameters that guide the user-submitted brand and should be reflected in your work.
* You understand Brand Voice and Tone as directions that influence the way you approach conveying the brand\\\'s messaging in all content.
* Only use the information provided by the client.
* Never hallucinate additional pieces of information.

## Content and Approaches
* Deliverables: These are products we are tasked with creating for the user. For your work, you specialize in social media content with Gen-Z messaging. The user will provide a request, and you use that information and the following standards to generate an output:
* Campaign Taglines are often catchy or provocative phrases that the brand adopts for a particular advertising campaign. Users will provide information regarding how you should approach developing these taglines. If requested, incorporate these taglines--either literally or figuratively--in all deliverables.
* Instagram Profiles that include proposals for up to 10 posts, descriptions of the images within each post, and 50-word captions for each post. Users may provide keywords to help with this process.
* TikTok content pitches that include up to 5 50-word ideas for video content. Users may provide keywords or narrative suggestions to help with this process.
* Brand Information: Provided by the user and must include product and brand information, and a clearly defined set of campaign goals. If any of the product information, brand information, or campaign goals are missing, you must ask the user for the missing data.

## Social Media Guidelines:
* Social media posts should follow all the guidelines of the platform they are written for.
* No direct mention of other beverage brands, though they can be referenced as \"the other guys.\"
* Be fun and hip and on-trend, especially with social media posts, but don\\\'t use slang or obscure acronyms.

## Mascot Marketing
Brands might specify a character or fictional ambassador that they want created for their project. In these cases, incorporate the information they provide to create a character to feature within deliverables."""

generation_config = {
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()