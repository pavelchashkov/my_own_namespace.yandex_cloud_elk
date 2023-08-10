#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt) # noqa: E501
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: my_own_module

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: path to the file
        required: true
        type: str
    content:
        description: content write to the file
        required: false
        type: str
        default: ''
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Pavel Chashkov (@pavelchashkov)
"""

EXAMPLES = r"""
# Pass in a message
- name: Test with a valid path (folder with path /tmp/ exist)
  my_namespace.my_collection.my_own_module:
    path: /tmp/test
    content: test

# fail the module
- name: Test failure of the module (folder with path /no_folder/ does not exist exist) # noqa: E501
  my_namespace.my_collection.my_test:
    path: /no_folder/test
    content: test
"""

RETURN = r"""
# These are examples of possible return values, and in general should use other names for return values. # noqa: E501
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
message:
    description: The output message that the test module generates.
    type: str
    returned: always
"""

from ansible.module_utils.basic import AnsibleModule  # noqa: E402


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type="str", required=True),
        content=dict(type="str", required=False, default=""),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(changed=False, failed=False, original_message="", message="")

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    file_path = module.params["path"]
    content = module.params["content"]

    try:
        with open(file_path, "w") as f:
            f.write(content)
    except Exception as err:
        module.fail_json(msg=f"Fail save conten to the file, {err}", **result)
    else:
        result["changed"] = True

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result["original_message"] = file_path
    result["message"] = "success save content to the file"

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    # if module.params["name"] == "fail me":
    #     module.fail_json(msg="You requested this to fail", **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
