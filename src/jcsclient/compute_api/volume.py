# Copyright (c) 2016 Jiocloud.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

from jcsclient import utils
from jcsclient import requestify

def attach_volume(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--instance-id', required=True)
    parser.add_argument('--volume-id', required=True)
    parser.add_argument('--device', required=True)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def detach_volume(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--instance-id', required=False)
    parser.add_argument('--volume-id', required=True)
    parser.add_argument('--force', type=bool, required=False)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def show_delete_on_termination_flag(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--volume-id', required=True)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def update_delete_on_termination_flag(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--volume-id', required=True)
    parser.add_argument('--delete-on-termination', type=bool, required=True)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def create_volume(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--size', type=int, required=False)
    parser.add_argument('--snapshot-id', required=False)
    parser.add_argument('--encrypted', type=bool, required=False)
    parser.add_argument('--volume-type', required=False)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def delete_volume(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--volume-id', required=True)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def describe_volumes(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--volume-ids', nargs='+', required=False)
    parser.add_argument('--max-results', type=int, required=False)
    parser.add_argument('--next-token', required=False)
    parser.add_argument('--detail', type=bool, required=False)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)




