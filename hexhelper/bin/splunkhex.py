import re, sys, time, splunk.Intersplunk


def _hexencode(asciistring):
    return asciistring.encode('hex')


def _hexdecode(string):
    return string.decode('hex')


def _hexdecodeclean(hexstring):
    ascii = _hexdecode(hexstring)
    return ''.join([i if ord(i) < 128 else '?' for i in ascii])


def dohex(results, settings):
    try:
        fields, argvals = splunk.Intersplunk.getKeywordsAndOptions()
        actionstr = argvals.get("action", "decode")

        if actionstr == "encode":
            meth = _hexencode
        if actionstr == "decode":
            meth = _hexdecode
        if actionstr == "decodeclean":
            meth = _hexdecodeclean

        for r in results:
            for f in fields:
                if f in r:
                    r[f] = meth(r[f])

        splunk.Intersplunk.outputResults(results)

    except:
        import traceback

        stack = traceback.format_exc()
        results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))


results, dummyresults, settings = splunk.Intersplunk.getOrganizedResults()
results = dohex(results, settings)


