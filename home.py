import guidance
from guidance import select, models, gen

model = models.LlamaCpp('/Users/gavi/.cache/lm-studio/models/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf')
def get_command(model,input):
    devices={
        "devices": {
            "none":{
                "actions":"none"
            },
            "lights": {
                "actions": {
                    "turn_on": {},
                    "turn_off": {},
                    "dim": {
                        "range": {
                            "min": 0,
                            "max": 100,
                            "unit": "%"
                        }
                    },
                    "change_color": {
                        "colors": ["red", "green", "blue", "white", "yellow", "purple"]
                    }
                }
            },
            "thermostat": {
                "actions": {
                    "set_temperature": {
                        "range": {
                            "min": 60,
                            "max": 80,
                            "unit": "F"
                        }
                    },
                    "turn_off": {}
                }
            },
            "television": {
                "actions": {
                    "turn_on": {},
                    "turn_off": {},
                    "change_channel": {
                        "range": {
                            "min": 1,
                            "max": 500
                        }
                    },
                    "adjust_volume": {
                        "range": {
                            "min": 0,
                            "max": 100,
                            "unit": "%"
                        }
                    },
                    "mute": {}
                }
            },
            "smart_speaker": {
                "actions": {
                    "play_music": {},
                    "set_volume": {
                        "range": {
                            "min": 0,
                            "max": 100,
                            "unit": "%"
                        }
                    },
                    "set_alarm": {
                        "time_format": "HH:MM"
                    }
                }
            }
        }
    }

    model +=  f'''You are a home assistant. You can choose one of these devices, actions and values - {devices}. You can answer with device none if the question is not pertainant. The input from the user is -{input}. device:"{gen('device',stop='"',max_tokens=50)}",action:"{gen('action',stop='"',max_tokens=50)}",value:"{gen('value',stop='"',max_tokens=50)}"'''
    return (model.get('device'),model.get('action'),model.get('value'))

#print(get_command(model,"reduce volume"))

print(get_command(model,"set alarm for 7 in the morning"))