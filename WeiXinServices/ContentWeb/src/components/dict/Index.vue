<template>
    <div class="container">
        <div class="weui-cells">
            <div class="weui-cell weui-cell_access">
                <div class="weui-cell__hd"><label class="weui-label">关键字</label></div>
                <div class="weui-cell__bd">
                    <input v-model="keyword" class="weui-input" placeholder="请输入关键字">

                </div>
                <div class="weui-cell__bd" style="position: relative;margin-right: 10px;">
                    <a style="width: 80px;display: block" v-on:click="query()" class="weui-btn weui-btn_mini weui-btn_primary">查询</a>
                    <span class="weui-badge" style="position: absolute;top: -.4em;right: .6em;">{{psgdata.length}}</span></div>
            </div>
            
        </div>
            

        <div v-for="psg in psgdata">
            <div class="page">
                <div class="page__hd">
                    <div class="weui-cell weui-cell_access">
                        <div class="weui-cell__hd"> <h1 class="page__title">{{psg.name}}</h1></div>
                        <div class="weui-cell__bd">
                            <span class="weui-badge">{{psg.recodes.length}}</span>
                        </div>
                       
                        <p class="page__desc">别名：{{psg.names}}</p>
                    </div>
                </div>
                    <div class="page__bd" v-for="rec in psg.recodes">
                        <article class="weui-article">
                            <h2 class="title">{{ rec.refbook }}</h2>
                            <section>
                                
                                <section v-for="psec in Object.keys(rec)">
                                    <h3>{{psec}}</h3>
                                    <p>
                                        {{rec[psec]}}
                                    </p>

                                </section>

                            </section>
                        </article>
                    </div>

                </div>
        </div>
    </div>
</template>

<script>
    import { goGet } from '../../../api/axios.js'

    export default {
        name: "YaoCaiSearch",
        data: () => {
            return {
                psgdata: "",
                keyword: ""
            };
        },
        methods: {
            query: function () {
                if (this.keyword) {
                    goGet("http://localhost:3080/yaocai/search", { "key": this.keyword }).then((res) => {
                        this.psgdata = res.data;
                    })
                }
            }
        }
    }
</script>
<style lang="css" src="../../assets/weui.min.css"></style>
<style scoped>
</style>