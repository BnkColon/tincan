# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class YesterdayList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the YesterdayList

        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayList
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayList
        """
        super(YesterdayList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Usage/Records/Yesterday.json'.format(**self._solution)

    def stream(self, category=values.unset, start_date=values.unset,
               end_date=values.unset, limit=None, page_size=None):
        """
        Streams YesterdayInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param YesterdayInstance.Category category: The category
        :param date start_date: The start_date
        :param date end_date: The end_date
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            category=category,
            start_date=start_date,
            end_date=end_date,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, category=values.unset, start_date=values.unset,
             end_date=values.unset, limit=None, page_size=None):
        """
        Lists YesterdayInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param YesterdayInstance.Category category: The category
        :param date start_date: The start_date
        :param date end_date: The end_date
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance]
        """
        return list(self.stream(
            category=category,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, category=values.unset, start_date=values.unset,
             end_date=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of YesterdayInstance records from the API.
        Request is executed immediately

        :param YesterdayInstance.Category category: The category
        :param date start_date: The start_date
        :param date end_date: The end_date
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of YesterdayInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayPage
        """
        params = values.of({
            'Category': category,
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return YesterdayPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YesterdayList>'


class YesterdayPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the YesterdayPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayPage
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayPage
        """
        super(YesterdayPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of YesterdayInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        """
        return YesterdayInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YesterdayPage>'


class YesterdayInstance(InstanceResource):

    class Category(object):
        AUTHY_AUTHENTICATIONS = "authy-authentications"
        AUTHY_CALLS_OUTBOUND = "authy-calls-outbound"
        AUTHY_MONTHLY_FEES = "authy-monthly-fees"
        AUTHY_PHONE_INTELLIGENCE = "authy-phone-intelligence"
        AUTHY_PHONE_VERIFICATIONS = "authy-phone-verifications"
        AUTHY_SMS_OUTBOUND = "authy-sms-outbound"
        CALL_PROGESS_EVENTS = "call-progess-events"
        CALLERIDLOOKUPS = "calleridlookups"
        CALLS = "calls"
        CALLS_CLIENT = "calls-client"
        CALLS_GLOBALCONFERENCE = "calls-globalconference"
        CALLS_INBOUND = "calls-inbound"
        CALLS_INBOUND_LOCAL = "calls-inbound-local"
        CALLS_INBOUND_MOBILE = "calls-inbound-mobile"
        CALLS_INBOUND_TOLLFREE = "calls-inbound-tollfree"
        CALLS_OUTBOUND = "calls-outbound"
        CALLS_RECORDINGS = "calls-recordings"
        CALLS_SIP = "calls-sip"
        CALLS_SIP_INBOUND = "calls-sip-inbound"
        CALLS_SIP_OUTBOUND = "calls-sip-outbound"
        CARRIER_LOOKUPS = "carrier-lookups"
        CONVERSATIONS = "conversations"
        CONVERSATIONS_API_REQUESTS = "conversations-api-requests"
        CONVERSATIONS_CONVERSATION_EVENTS = "conversations-conversation-events"
        CONVERSATIONS_ENDPOINT_CONNECTIVITY = "conversations-endpoint-connectivity"
        CONVERSATIONS_EVENTS = "conversations-events"
        CONVERSATIONS_PARTICIPANT_EVENTS = "conversations-participant-events"
        CONVERSATIONS_PARTICIPANTS = "conversations-participants"
        IP_MESSAGING = "ip-messaging"
        IP_MESSAGING_COMMANDS = "ip-messaging-commands"
        IP_MESSAGING_DATA_STORAGE = "ip-messaging-data-storage"
        IP_MESSAGING_DATA_TRANSFER = "ip-messaging-data-transfer"
        IP_MESSAGING_ENDPOINT_CONNECTIVITY = "ip-messaging-endpoint-connectivity"
        LOOKUPS = "lookups"
        MEDIASTORAGE = "mediastorage"
        MMS = "mms"
        MMS_INBOUND = "mms-inbound"
        MMS_INBOUND_LONGCODE = "mms-inbound-longcode"
        MMS_INBOUND_SHORTCODE = "mms-inbound-shortcode"
        MMS_OUTBOUND = "mms-outbound"
        MMS_OUTBOUND_LONGCODE = "mms-outbound-longcode"
        MMS_OUTBOUND_SHORTCODE = "mms-outbound-shortcode"
        MONITOR_READS = "monitor-reads"
        MONITOR_STORAGE = "monitor-storage"
        MONITOR_WRITES = "monitor-writes"
        NUMBER_FORMAT_LOOKUPS = "number-format-lookups"
        PHONENUMBERS = "phonenumbers"
        PHONENUMBERS_CPS = "phonenumbers-cps"
        PHONENUMBERS_EMERGENCY = "phonenumbers-emergency"
        PHONENUMBERS_LOCAL = "phonenumbers-local"
        PHONENUMBERS_MOBILE = "phonenumbers-mobile"
        PHONENUMBERS_SETUPS = "phonenumbers-setups"
        PHONENUMBERS_TOLLFREE = "phonenumbers-tollfree"
        PREMIUMSUPPORT = "premiumsupport"
        RECORDINGS = "recordings"
        RECORDINGSTORAGE = "recordingstorage"
        SHORTCODES = "shortcodes"
        SHORTCODES_CUSTOMEROWNED = "shortcodes-customerowned"
        SHORTCODES_MMS_ENABLEMENT = "shortcodes-mms-enablement"
        SHORTCODES_MPS = "shortcodes-mps"
        SHORTCODES_RANDOM = "shortcodes-random"
        SHORTCODES_UK = "shortcodes-uk"
        SHORTCODES_VANITY = "shortcodes-vanity"
        SMS = "sms"
        SMS_INBOUND = "sms-inbound"
        SMS_INBOUND_LONGCODE = "sms-inbound-longcode"
        SMS_INBOUND_SHORTCODE = "sms-inbound-shortcode"
        SMS_OUTBOUND = "sms-outbound"
        SMS_OUTBOUND_LONGCODE = "sms-outbound-longcode"
        SMS_OUTBOUND_SHORTCODE = "sms-outbound-shortcode"
        TASKROUTER_TASKS = "taskrouter-tasks"
        TOTALPRICE = "totalprice"
        TRANSCRIPTIONS = "transcriptions"
        TRUNKING_CPS = "trunking-cps"
        TRUNKING_EMERGENCY_CALLS = "trunking-emergency-calls"
        TRUNKING_ORIGINATION = "trunking-origination"
        TRUNKING_ORIGINATION_LOCAL = "trunking-origination-local"
        TRUNKING_ORIGINATION_MOBILE = "trunking-origination-mobile"
        TRUNKING_ORIGINATION_TOLLFREE = "trunking-origination-tollfree"
        TRUNKING_RECORDINGS = "trunking-recordings"
        TRUNKING_SECURE = "trunking-secure"
        TRUNKING_TERMINATION = "trunking-termination"
        TURNMEGABYTES = "turnmegabytes"
        TURNMEGABYTES_AUSTRALIA = "turnmegabytes-australia"
        TURNMEGABYTES_BRASIL = "turnmegabytes-brasil"
        TURNMEGABYTES_IRELAND = "turnmegabytes-ireland"
        TURNMEGABYTES_JAPAN = "turnmegabytes-japan"
        TURNMEGABYTES_SINGAPORE = "turnmegabytes-singapore"
        TURNMEGABYTES_USEAST = "turnmegabytes-useast"
        TURNMEGABYTES_USWEST = "turnmegabytes-uswest"

    def __init__(self, version, payload, account_sid):
        """
        Initialize the YesterdayInstance

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        """
        super(YesterdayInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'category': payload['category'],
            'count': payload['count'],
            'count_unit': payload['count_unit'],
            'description': payload['description'],
            'end_date': deserialize.iso8601_date(payload['end_date']),
            'price': deserialize.decimal(payload['price']),
            'price_unit': payload['price_unit'],
            'start_date': deserialize.iso8601_date(payload['start_date']),
            'subresource_uris': payload['subresource_uris'],
            'uri': payload['uri'],
            'usage': payload['usage'],
            'usage_unit': payload['usage_unit'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
        }

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The api_version
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def category(self):
        """
        :returns: The category
        :rtype: YesterdayInstance.Category
        """
        return self._properties['category']

    @property
    def count(self):
        """
        :returns: The count
        :rtype: unicode
        """
        return self._properties['count']

    @property
    def count_unit(self):
        """
        :returns: The count_unit
        :rtype: unicode
        """
        return self._properties['count_unit']

    @property
    def description(self):
        """
        :returns: The description
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def end_date(self):
        """
        :returns: The end_date
        :rtype: date
        """
        return self._properties['end_date']

    @property
    def price(self):
        """
        :returns: The price
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: The price_unit
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def start_date(self):
        """
        :returns: The start_date
        :rtype: date
        """
        return self._properties['start_date']

    @property
    def subresource_uris(self):
        """
        :returns: The subresource_uris
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def usage(self):
        """
        :returns: The usage
        :rtype: unicode
        """
        return self._properties['usage']

    @property
    def usage_unit(self):
        """
        :returns: The usage_unit
        :rtype: unicode
        """
        return self._properties['usage_unit']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YesterdayInstance>'
