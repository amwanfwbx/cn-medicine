<template>
    <div class="container">
        <SearchBar v-bind:txt="keyword" v-bind:propitems="hitsdata" v-on:search="query" v-on:hit="prop" ref="sbar"></SearchBar>
        


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
    import SearchBar from '../searchbar.vue'

    export default {
        name: "YaoCaiSearch",
        components: { SearchBar },
        data: () => {
            return {
                psgdata: "",
                keyword: "",
                hitsdata:[]
            };
        },
        methods: {
            query: function () {
                if (this.$refs.sbar.keyword) {
                    goGet("http://localhost:3080/yaocai/search", { "key": this.$refs.sbar.keyword }).then((res) => {
                        this.psgdata = res.data;
                    })
                }
            },
            prop: function (evt) {
                if (this.$refs.sbar.keyword) {
                    goGet("http://localhost:3080/yaocai/hits/" + this.$refs.sbar.keyword).then((res) => {
                        this.hitsdata = res.data;
                    })
                }
            }
        }
    }
</script>
<style lang="css" src="../../assets/weui.min.css"></style>
<style scoped>
</style>