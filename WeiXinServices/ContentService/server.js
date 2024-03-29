const Koa = require('koa');
const route = require('./route')
const MongoClient = require('mongodb').MongoClient;


const ObjectId = require('mongodb').ObjectId;
const app = new Koa();
const co = require('co');

// Connection URL
const dburl = 'mongodb://localhost:27017/eat';
const client = new MongoClient(dburl, { useNewUrlParser: true, useUnifiedTopology: true });

route.route("/yaocai/search", async (ctx) => {

    if (!ctx.query.key) return;
    res = null;
    try {
        // Use connect method to connect to the Server
        await client.connect();

        const db = client.db();
        res = await db.collection("yaocai_info").find({ "names": ctx.query.key }).toArray();;
        
    } catch (err) {
        console.log(err.stack);
    }

    client.close();
    return res;
});
route.route("/yaocai/hits/{key}", async (ctx) => {
    return co(function* () {
        try {
            var conn = yield client.connect();
            var db = conn.db();
            var names = yield db.collection("yaocai_info").find({ "names": { $regex: decodeURIComponent(ctx.urlps.key) } }).project({ _id: 1, name: 1, names: 1 }).limit(10).toArray();
            client.close();
            return names;
        } catch (err) {
            console.log(err.stack);
        }
    });
});
route.route("/yaocai/{ycid}", async (ctx) => {
    console.log("��ѯyaocai:" + ctx.urlps.ycid);
    res = null;
    try {
        // Use connect method to connect to the Server
        await client.connect();

        const db = client.db();
        res = await db.collection("yaocai_info").findOne({ "_id": ObjectId(ctx.urlps.ycid)});
    } catch (err) {
        console.log(err.stack);
    }

    client.close();
    return res;
});

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
  
    
    ctx.set("Access-Control-Allow-Origin", "http://localhost:1337");
    ctx.set("Access-Control-Allow-Methods", "POST,GET");
    ctx.set("Access-Control-Allow-Credentials","true");
    ctx.set("Access-Control-Allow-Headers", "X-Requested-With");

});

// response
app.use(async ctx => {
    await route.apply(ctx);
});

app.listen(3080);