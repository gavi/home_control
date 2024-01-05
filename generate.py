from guidance import models, gen, select
import guidance

# Define devices and their actions/information requests
devices = {
    "lights": {
        "actions": ["turn on", "turn off", "dim", "brighten"],
        "info": ["current status", "brightness level"]
    },
    "thermostat": {
        "actions": ["set temperature", "turn off"],
        "info": ["current temperature", "status"]
    },
    "television": {
        "actions": ["turn on", "turn off", "change channel", "adjust volume"],
        "info": ["current channel", "volume level"]
    }
}

@guidance
def device_interaction(lm):
    # Choose between action and information request
    lm += "Do you want to perform an action or request information? " + select(["action", "information"], name='interaction_type') + "\n"

    # Select a device
    lm += "Which device are you interested in? " + select(list(devices.keys()), name='device') + "\n"
    device = lm['device']

    # Provide relevant options based on interaction type
    interaction_type = lm['interaction_type']
    options = devices[device][interaction_type]
    lm += f"Choose an option for the {device}: " + select(options, name='option') + "\n"

    # Construct the JSON output
    option = lm['option']
    json_output = {
        "device": device,
        "interaction_type": interaction_type,
        "command": option
    }
    lm += f"JSON Output: {json_output}"

    return lm

# Example usage
lm = models.LlamaCpp('/Users/gavi/.cache/lm-studio/models/TheBloke/zephyr-7B-beta-GGUF/zephyr-7b-beta.Q8_0.gguf')
lm += device_interaction()
