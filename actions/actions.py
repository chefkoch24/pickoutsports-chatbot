# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionLeague(Action):

    def name(self) -> Text:
        return "action_league"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        league = tracker.get_slot("league")
        print(type(league))
        print(league)
        if league is not None:
            league = league.lstrip()
        if league == 'bundesliga':
            dispatcher.utter_message(text="DAZN & Sky")
        elif league == 'premier league':
            dispatcher.utter_message(text="Sky")
        elif league == 'champions league':
            dispatcher.utter_message(text="Sky & DAZN")
        elif league == 'europa league':
            dispatcher.utter_message(text="DAZN")
        else:
            dispatcher.utter_message(text="Diese Liga kenne ich leider nicht. Bitte gib eine Liga ein.")

        return []
