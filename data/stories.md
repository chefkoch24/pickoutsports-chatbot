## league
 * greet
  - utter_greet
  - utter_how_can_i_help_you
 * inform{"league": "bundesliga"}
  - action_league
 * thanks
  - utter_goodbye

## league
* inform{"league": "bundesliga"}
  - action_league
  
<!--## bundesliga 
 * greet
  - utter_greet
  - utter_how_can_i_help_you
 * bundesliga
  - utter_bundesliga
 * thanks
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
