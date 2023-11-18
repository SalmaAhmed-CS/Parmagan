from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
import requests
import openai
from IPython.display import Image, display


def first (word):
    # reem code
    openai.api_key = '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'

    def get_completion(prompt, model="gpt-3.5-turbo"):

        messages = [{"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(

            model=model,

            messages=messages,

            temperature=0,

        )
        # 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

        return response.choices[0].message["content"]
        ### end code reem ###

    ### ah mogam api


    url = "https://siwar.ksaa.gov.sa/api/alriyadh/search?query=" + word
    headers = {
        'accept': 'application/json',
        'apikey': '8c7a76bb-8d1a-404b-b579-5a0066f3ba02'
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()

        # Process the data as needed for your AI purpose

    ### end

        extracted_data = []

        for entry in data:
            # Extract the word form
            word_form = entry.get("lemma", {}).get("formRepresentations", [{}])[0].get("form", "")

            for sense in entry.get("senses", []):
                # Extract definition
                definition = sense.get("definition", {}).get("textRepresentations", [{}])[0].get("form", "")

                # Extract examples
                examples = [ex.get("form", "") for ex in sense.get("examples", []) if ex.get("form")]
                prompt = "معنى كلمة " + word_form + "هو " + definition + "فهل كلمة " + word_form + "تعتبر ملموس أو غير ملموس ثم ضعها لي في مثال واحد فقط لا ديني وضع لي النتيجة بالشكل التالي:\nالكلمة:\n معناها:\n هل تعتبر ملموس أو غير ملموس:\n المثال:  "
                examples_Sadaf_1 = get_completion(prompt)
                print(examples_Sadaf_1)
                examples_Sadaf = examples_Sadaf_1.split("المثال:")[1]

                # salwa code
                Reem_output = examples_Sadaf_1

                prompt = Reem_output.split("\n")


                prompt[2] = prompt[2].replace("هل تعتبر ملموس أو غير ملموس:", "")
                prompt[3] = prompt[3].replace("المثال:", "")

                prompts = ""
                if "محسوس" in prompt[2]:
                    prompts = prompt[3]
                elif "فعل مضارع" not in definition and "جمع التكسير" not in definition:
                    prompts = word_form + ": " + definition
                else:
                    prompts = prompt[3]

                # Set your OpenAI API key
                openai.api_key = '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'

                string = "قم برسم المثال الذي يظهر بالنص التالي: \n"

                # Make a request to the DALL-E 3 API
                response = openai.Image.create(
                    model="dall-e-3",

                    prompt=string + prompts,
                    n=1
                )

                # Assuming the image URL is in the first element of the 'data' list
                image_url = response['data'][0]['url']

                # Display the image
                # display(Image(url=image_url))
                ###### end salwa code ####

                extracted_data.append({
                    "word_form": word_form,
                    "definition": definition,
                    "examples": examples,
                    "examples_Sadaf": examples_Sadaf,
                    "image_url": image_url,

                })
        return extracted_data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Failed to fetch data: {response.status_code}"




def scound (word):
    openai.api_key = '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'

    def get_completion(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]

    dic = {}
    dic["و"] = ['التمثيل', 'سبب ضمني', 'إعادة الصياغة', 'الاستثناء', 'الخلفية', 'تشبيه', 'نتيجة ضمنية', 'التضاد',
                'سبب مباشر', 'الشرطية', 'الربط', 'نتيجة مباشرة', 'التزامن', 'الترتيب الزمني']
    dic["ل"] = ['سبب ضمني', 'نتيجة ضمنية', 'التضاد', 'سبب مباشر', 'الترتيب الزمني']

    dic["لكن"] = ["تضاد", "ربط", "اعادة صياغة", "تمثيل"]
    dic["بعد"] = ["ترتيب زمني", "سبب مباشر", "سبب ضمني", "تضاد", "نتيجة ضمنية", "نتيجة مباشرة"]
    dic["خلال"] = ["تزامن"]
    dic["ف"] = ["نتيجة مباشرة", "سبب مباشر", "سبب ضمني", "نتيجة ضمنية", "اعادة صياغة", "تمثيل", "تزامن", "ترتيب زمني",
                "تضاد", "خلفية"]
    dic["ب"] = ["سبب مباشر", "سبب ضمني", "تزامن", "تضاد"]
    dic["قبل"] = ["ترتيب زمني", "سبب مباشر"]
    dic["لان"] = ["سبب مباشر"]
    dic["لأن"] = ["سبب مباشر"]
    dic["منذ"] = ['ترتيب زمني', "تزامن", "سبب ضمني", "سبب مباشر"]
    dic["كما"] = ['الترتيب الزمني',
                  'التزامن',
                  'سبب ضمني',
                  'التضاد',
                  'التمثيل',
                  'تشبيه',
                  'الربط']
    dic["اثر"] = ['الترتيب الزمني', 'سبب مباشر']
    dic["إثر"] = ['الترتيب الزمني', 'سبب مباشر']

    dic["بسبب"] = ['الترتيب الزمني',
                   'التزامن',
                   'نتيجة مباشرة',
                   'سبب مباشر',
                   'الشرطية',
                   'التضاد',
                   'تشبيه']
    dic["الا ان"] = ['سبب مباشر']
    dic["إلا أن"] = ['سبب مباشر']
    dic["فيما"] = ["الربط", "الاستثناء", "التضاد"]
    dic["ثم"] = ['نتيجة مباشرة', 'سبب مباشر', 'التضاد']
    dic["او"] = ['التكامل', 'تخيير تضاد']
    dic["أو"] = ['التكامل', 'تخيير تضاد']
    dic["في حال"] = ['الشرطية']
    dic["اذا"] = ['الشرطية']
    dic["إذا"] = ['الشرطية']
    dic['حيث'] = ['التمثيل', 'سبب ضمني', 'إعادة الصياغة', 'الخلفية', 'سبب مباشر', 'الربط', 'نتيجة مباشرة', 'التزامن']
    dic["رغم"] = ['التضاد']
    dic["حتى"] = ['نتيجة ضمنية', 'التضاد', 'سبب مباشر', 'الشرطية', 'الربط', 'نتيجة مباشرة', 'التزامن']
    dic["في حين"] = ['التضاد', 'التزامن', 'الربط']
    dic["اما"] = ['التضاد', 'الربط', 'الترتيب الزمني']
    dic["أما"] = ['التضاد', 'الربط', 'الترتيب الزمني']
    dic["خصوصا"] = ['التمثيل', 'سبب ضمني', 'سبب مباشر', 'إعادة الصياغة']
    dic["بعدما"] = ['التضاد', 'سبب ضمني', 'سبب مباشر', 'الترتيب الزمني']
    dic["اذ"] = ['سبب ضمني', 'إعادة الصياغة', 'نتيجة ضمنية', 'سبب مباشر', 'الربط', 'التمثيل']
    dic["إذ"] = ['سبب ضمني', 'إعادة الصياغة', 'نتيجة ضمنية', 'سبب مباشر', 'الربط', 'التمثيل']
    dic["بينما"] = ['التضاد', 'التزامن']
    dic["بل"] = ['التضاد', 'الربط', 'إعادة الصياغة']
    dic["بهدف"] = ['سبب مباشر']
    dic["بالتالي"] = ['نتيجة ضمنية', 'نتيجة مباشرة']
    dic["جراء"] = ['سبب مباشر']
    dic["على الرغم"] = ["تضاد"]
    dic["نظرا ل"] = ["سبب ضمني"]
    dic["انما"] = ['التضاد', 'نتيجة مباشرة', 'سبب مباشر', 'الربط']
    dic["إنما"] = ['التضاد', 'نتيجة مباشرة', 'سبب مباشر', 'الربط']

    dic["لو"] = ['نتيجة ضمنية', 'التضاد', 'الشرطية']
    dic["في ظل"] = ['التزامن', 'سبب مباشر']
    dic["بيد ان"] = ["تضاد"]
    dic["رغم ان"] = ["تضاد"]
    dic["غير ان"] = ["تضاد"]
    dic["فضلا عن"] = ["ربط"]
    dic["كذلك"] = ["ربط"]
    dic["عقب"] = ['سبب ضمني', 'سبب مباشر', 'الترتيب الزمني']
    dic["لاسيما"] = ['التمثيل', 'سبب مباشر', 'إعادة الصياغة']
    dic["الا بعد"] = ['الاستثناء', 'الشرطية']
    dic["بفضل"] = ["سبب مباشر"]
    dic["قبيل"] = ["ترتيب زمني"]
    dic["في المقابل"] = ["تضاد"]
    dic["بالرغم من"] = ["تضاد"]
    dic["لكي"] = ['سبب مباشر']
    dic["بغية"] = ["سبب مباشر"]
    dic["طالما"] = ['سبب مباشر', 'الشرطية']
    dic["من ثم"] = ['نتيجة مباشرة', 'الترتيب الزمني']
    dic["بالمقابل"] = ['التضاد', 'الربط']
    dic["الا"] = ['الاستثناء']
    dic["نتيجة"] = ["سبب ضمني", "سبب مباشر"]
    dic["بالإضافة إلى"] = ["ربط"]
    dic["لأن"] = ["سبب مباشر"]
    dic["قبل ان"] = ["ترتيب زمني"]
    dic['حال'] = ["ربط", "شرطية"]
    dic['الا اذا'] = ['استثناء', 'شرطية']
    dic["حينها"] = ['تزامن']
    dic["كي"] = ["سبب مباشر"]
    dic["بيد"] = ["تضاد"]
    dic["اضافة الى"] = ['ربط']
    dic['كأن'] = ["تمثيل"]
    dic["بحيث"] = ["نتيجة مباشرة"]
    dic["حين"] = ['تزامن']
    dic['خلافا ل'] = ['تضاد']
    dic['برغم'] = ['تضاد']
    dic["كلما"] = ['شرطية']
    dic['لذا'] = ['سبب مباشر']
    dic['لذلك'] = ['نتيجة مباشرة']
    dic['بمعنى آخر'] = ['إعادة الصياغة']
    dic['لولا'] = ['شرطية']
    dic["بيد أن"] = ["تضاد"]
    dic["رغم أن"] = ["تضاد"]
    dic["غير أن"] = ["تضاد"]
    dic["فضلا عن"] = ["ربط"]
    dic["إلا بعد"] = ['الاستثناء', 'الشرطية']

    dic["إلا"] = ['الاستثناء']

    dic["بالإضافة إلى"] = ["ربط"]

    dic["قبل أن"] = ["ترتيب زمني"]

    dic['إلا إذا'] = ['استثناء', 'شرطية']

    dic["إضافة إلى"] = ['ربط']
    one = []


    url = "https://siwar.ksaa.gov.sa/api/alriyadh/search?query=" + word
    headers = {
        'accept': 'application/json',
        'apikey': '8c7a76bb-8d1a-404b-b579-5a0066f3ba02'
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        print("### ", word)
        if word in dic:
            data = response.json()
            types = " ".join(dic[word])

            print(types)

            # Examples
            all_ans = []
            for i in range(len(dic[word])):
                prompt = f"ضع كلمة '{word}' في جملة واحدة مفيدة لا دينية بحيث تدل على العلاقة التالية: {dic[word][i]}. وضع النتيجة في الشكل التالي:\nالكلمة:\nالعلاقة:\nالجملة:"
                print(prompt)
                response = get_completion(prompt)
                one = response.split("\n")
                all_ans.append({
                    "word": one[1],
                    "relationship": one[3],
                    "sentence": one[5],
                })

            return  all_ans
        else:
            print(f"Word '{word}' not found in the dictionary.")
            return  "Word '{word}' not found in the dictionary"
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return  "Failed to fetch data: {response.status_code}"

def index(request):
    if request.method == 'POST':
        word = request.POST['word']
        extracted_data = first(word)
        # all_ans = scound(word)
        return render(request, 'index.html', {"extracted_data": extracted_data})
        # return render(request, 'index.html',{"extracted_data":extracted_data,"all_ans":all_ans} )
    else:
       return render(request, 'index.html')
>>>>>>> 43c7541 (scound commit)
