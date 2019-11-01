const ContentType_JSON = "application/json";

routes = [];

function match(pattern, ctx) {
    urlParam = {};
    url = ctx.url;
    var idx_url = 0;
    for (var i = 0; i < pattern.length; i++) {
        if (pattern[i] == url[idx_url]) {
            idx_url = i + 1;
            continue;
        }
        else if (pattern[i] == "{") {
            psend_idx = pattern.indexOf("}", i);
            ps_name = pattern.substring(i+1, psend_idx);
            for (var x = idx_url; x < url.length; x++) {
                if (url[x] == '/' || url[x] == '?' || url[x] == '&' || x == url.length - 1) {
                    //提取
                    urlParam[ps_name] = url.substring(i, x == url.length - 1 ? x + 1 : x);
                    //urlParam.push({ "name": ps_name, "val": url.substring(i, x == url.length - 1?x+1:x) });
                    idx_url = x;
                    break;
                }
            }

            i = psend_idx;
        } else {
            return false;
        }
    }

    return urlParam;
}
module.exports.route = function (url, bussFunc) {
    routes.push({ pattern: url, func: bussFunc });
};
module.exports.apply = async function (ctx) {
    for (i = 0; i < routes.length; i++) {
        r = routes[i];
        urlps = match(r.pattern, ctx);
        if (urlps) {
            ctx.urlps = urlps;
            
            await r.func(ctx).then(res => {
                if (res != null) ctx.response.body = res;
                ctx.type = ContentType_JSON;
            }).catch(err => {
                ctx.response.body = err;
                });
            
            return;
        }
    }
}
