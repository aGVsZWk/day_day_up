def generate_webform(text_fields=[], checkbox_fields=[]):
    generated_fields = "\n".join(
        map(lambda x: '{0}: <br><input type="text" name={0}><br>'.format(x),
            text_fields))

    generated_fields += "\n".join(
        map(
            lambda x:
            '{0}: <label><input type="checkbox" id="{0}" value="{0}"><br>'.
            format(x), checkbox_fields))
    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html_form(text_fields=[], checkbox_fields=[]):
    with open('form_file.html', 'w') as f:
        f.write("<html><body>{}</body></html>".format(
            generate_webform(text_fields=text_fields,
                             checkbox_fields=checkbox_fields)))


if __name__ == '__main__':
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ['awesome', 'bad']
    build_html_form(text_fields=text_fields, checkbox_fields=checkbox_fields)
