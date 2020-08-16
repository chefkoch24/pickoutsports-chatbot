## happy path
 * greet
  - utter_greet
  - utter_how_can_i_help_you
 * inform{"league": "bundesliga"}
  - action_league
 * thanks
  - utter_goodbye

## only league
* inform{"league": "bundesliga"}
  - action_league

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
