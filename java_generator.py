from jinja2 import Environment, FileSystemLoader
from itertools import product
import os


def get_class_name(model_with_implementation, transformation_present, lookup_table_present, property_io_present):
    class_name = ""
    if model_with_implementation:
        temp = model_with_implementation.split('-')
        class_name += temp[0]  # model name
        class_name += temp[1]  # implementation_name

    if not transformation_present:
        class_name += "No"

    class_name += "Transformation"

    if not lookup_table_present:
        class_name += "No"

    class_name += "LookupTable"
    if not property_io_present:
        class_name += "No"

    class_name += "PropertyIO"

    return class_name


def main(template_filename, target_directory):
    """

    :type template_filename: string
    :type target_directory: string
    """
    env = Environment(loader=FileSystemLoader('templates'))

    template = env.get_template(template_filename)

    model = ["GBM-SampleModel", "GBM-IncrementalModel", "GLM-SampleModel", "GLM-IncrementalModel",
             "MGBM-SampleModel", "MGBM-IncrementalModel", None]
    transformation = [True, False]
    lookup_table = [True, False]
    property_io = [True, False]

    whole_list = [model, transformation, lookup_table, property_io]

    # check for directory and create if needed
    if not os.path.isdir(target_directory):
        os.makedirs(target_directory)

    for (model_With_implementation, transformation_present, lookup_table_present, property_IO_present) in product(
            *whole_list):
        if not (model_With_implementation or transformation_present or lookup_table_present):
            continue

        render_dict = {}

        print(model_With_implementation, transformation_present, lookup_table_present, property_IO_present)

        # Decide class name
        render_dict["ClassName"] = "%sIntegrationTest" % get_class_name(model_With_implementation,
                                                                        transformation_present,
                                                                        lookup_table_present,
                                                                        property_IO_present)

        # create file in target_dir with filename and render template to this file
        with open(os.path.join(target_directory + os.sep + render_dict.get("ClassName") + ".java"), 'w') as fl:
            fl.write(template.render(render_dict))


if __name__ == "__main__":
    main("template_data.txt", "./temp1")
