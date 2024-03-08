import json
from fastapi import Depends

from app.apis.gecko import GeckoApi
from app.configs.settings import settings
from openai import OpenAI


class ChatGptHelper:
    def __init__(
            self,
            gecko_api: GeckoApi = Depends()
    ) -> None:
        self.chatgpt_client = OpenAI(api_key=settings.openai_api_key)
        self.gecko_api = gecko_api

    def handle(self, message: str) -> str:
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_cryptocurrency_price",
                    "description": "Get the current price of any cryptocurrencies in any other supported currencies that you need",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "Id of coins,, e.g. bitcoin, ethereum",
                            },
                            "currency": {
                                "type": "string",
                                "enum": ["USD", "IDR"],
                                "description": "Currency of coins. currently only support USD and IDR. If there is no currency the function return price in USD",
                            },
                        },
                        "required": ["id"],
                    },
                }
            },
        ]

        client = OpenAI(api_key=settings.openai_api_key)
        initial_prompt = ("You're hired as cryptocurrency consultant. "
                          "Here is your profile, "
                          "You are Jan Kristanto."
                          "Professional Background"
                          "You are an AI Engineering Manager at Waresix. "
                          "Prior to this, You served as a Principal Software Engineer at Indodana."
                          "Academic Pursuits"
                          "Driven by a thirst for knowledge, you pursued a Doctor of Philosophy (Ph.D.) in Computer Science from National Chiao Tung University Taiwan. "
                          )

        # initial_prompt = ("You're hired as cryptocurrency consultant.")

        messages = [
            {"role": "system", "content": initial_prompt},
            {"role": "user", "content": message}
        ]

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
            tools=tools,
            tool_choice="auto"
        )

        response = completion.choices[0].message
        tool_calls = response.tool_calls

        response_message = response.content

        if tool_calls:
            # Note: the JSON response may not always be valid; be sure to handle errors
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if function_name == "get_cryptocurrency_price":
                    crypto_price = self.gecko_api.get_current_price(
                        codename=function_args["id"]
                    )

                    content_cryptocurrency_price = "current " + function_args["id"] + " price is " + str(crypto_price[function_args["id"]]["usd"]) + " USD"

                    messages.append(
                        {
                            "role": "assistant",
                            "content": "I'm calling " + function_name + " to get current " + function_args["id"] + " price.",
                        }
                    )

                    messages.append(
                        {
                            "role": "assistant",
                            "content": content_cryptocurrency_price,
                        }
                    )

            second_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0
            )

            return second_response.choices[0].message.content

        return response_message
