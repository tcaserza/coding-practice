#
# PROBLEM: Given a dict of items (packages) with their respective dependencies, determine an order to install them
#


def resolve_dependencies(deps):
    for k,v in deps.iteritems():
        if k in order:
            continue
        print "examining item: %s, dependencies: %s" % (k,v)
        if k in order:
            continue
        if v is None:
            print "dependencies for %s are None, appending" % k
            order.append(k)
            continue
        for i in v.split(','):
            if i not in order:
                resolve_dependencies({i:dependencies[i]})
                print "dependency %s for %s is resolved" % (i, k)
            else:
                print "dependency %s for %s has already been resolved" % (i,k)
        print "all dependencies for %s are resolved, appending" % k
        order.append(k)



order = []
dependencies = {"0":None, "1":"0", "2":"0", "3":"1,2","4":"3"}
resolve_dependencies(dependencies)
print order
