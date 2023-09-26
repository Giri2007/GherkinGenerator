import json
from APIConnection.openAI import openAiConnect
from speechToText.speecText import speechText

global generated_text


class runnerFile:
    capi = openAiConnect()
    sc = speechText()
    input_prompt = sc.recognize_speech()
    access_key = capi.readData()
    result = capi.call_api(input_prompt, access_key)
    print(result)

    if result:
        generated_text = result["choices"][0]["text"]
        print(generated_text)
    else:
        print("error")

    destination_file_path = "D:\\AutomatedGherkin\\Output\\" + result["id"] + ".feature"

    with open(destination_file_path, "w") as destination_file:
        json.dump(generated_text, destination_file)
