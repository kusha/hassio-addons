from jinja2 import Template

def main():
    with open('template/config.json.jinja', 'r') as template_file:
        config_json_template = template_file.read()
    addons = [
        {
            "name": "Vacuum",
            "slug": "vacuum",
            "panel_icon": "mdi:robot-vacuum"
        }
    ]
    for addon in addons:
        # os.mkdir(addon["slug"])
        config = Template(config_json_template).render(**addon)
        print(config)


if __name__ == "__main__":
    main()