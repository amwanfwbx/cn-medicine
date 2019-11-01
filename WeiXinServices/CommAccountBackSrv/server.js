const Koa = require('koa');
const app = new Koa();

const test_appid = "wxf806ab261fccf763";
const test_key = "fe651a6677a5266bda5c4afdc158b14c";

const appid = "wx3af64873ef296463";
const aeskey = "GiG4KfLWKxb3lgsRNNGvCjRPYpGzejHcttHhO1PY0Ek"

const mytoken = "1ejsdjq928ujfjcsdjkl";
const skey = "42f232bb01523fa7dd05fc31488f5429"
const crypto = require('crypto');

var https = require("https");

testToken = "26_w5Wo_rp25l_uiz5SNUda4nrhnNEXQmJBt7OCshdQxZ0kN6DH1hPZqRpa4lsjnn1GS5-ZhxoTxwwcpmOo_UH_FxJws9stBayie7pKF6BOOHkWQQTTRyjf7tqrupERLXdAIAEYK";
accToken = "26_anqudWRxM_e8quVejdoP7ekkSopv7i5IRZ2npHj6Ry4sX4ztW9UZy9i7KBEwm2t9ZESHq88dXWmyQnJ1WnmVT6p8KxiRsDXLWp71zpjM5JF2i75vQx9jNqQyyIcQLUiACAVQZ";
// logger

app.use(async (ctx, next) => {
    await next();
    const rt = ctx.response.get('X-Response-Time');
    console.log(`${ctx.method} ${ctx.url} - ${rt}`);
    console.log(ctx.request.query);
});

// x-response-time

app.use(async (ctx, next) => {
    const start = Date.now();
    await next();
    const ms = Date.now() - start;
    ctx.set('X-Response-Time', `${ms}ms`);
});

// response

app.use(async ctx => {
    checksign(ctx);
    console.log(ctx.request);
});

function getAccToken() {
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx3af64873ef296463&secret=42f232bb01523fa7dd05fc31488f5429"
    https.get(url, function (res) {
        var buffer = [];
        res.on('data', function (data) {
            buffer.push(data);
        });
        res.on('end', function (data) {
            console.log(JSON.parse(Buffer.concat(buffer).toString()));
        });
    });
}

function checksign(ctx) {
    var signature = ctx.request.query.signature;
    var timestamp = ctx.request.query.timestamp;
    var nonce = ctx.request.query.nonce;

    var ori_arr = [testToken, timestamp, nonce].sort();
    var ori_str = ori_arr[0] + ori_arr[1] + ori_arr[2];

    var validStr = crypto.createHash('sha1').update(ori_str).digest('hex').toLowerCase();
    console.log("v:" + validStr);

    return signature == validStr;
}
app.listen(3000);