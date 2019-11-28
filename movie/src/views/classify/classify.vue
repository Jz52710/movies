<template>
    <div class="classify-box">
        <el-container>
            <el-row :span="24" style="display: flex">
                <el-col :span="24">
                    <el-breadcrumb separator="|" class="table-box">
                        <router-link tag="span" :to="{ path: 'action'}" class="mold-box"><span @click="action()">动作</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'war'}" class="mold-box"><span @click="war()">战争</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'science'}" class="mold-box"><span @click="science()">科幻</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'suspense'}" class="mold-box"><span @click="suspense()">悬疑</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'comedy'}" class="mold-box"><span @click="comedy()">喜剧</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'love'}" class="mold-box"><span @click="love()">爱情</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'inspiration'}" class="mold-box"><span @click="inspiration()">剧情</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'animation'}" class="mold-box"><span @click="animations()">动画</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'thriller'}" class="mold-box"><span @click="thriller()">惊悚</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'crime'}" class="mold-box"><span @click="crime()">犯罪</span></router-link>
                        <span style="margin: 0 6px">|</span>
                        <router-link tag="span" :to="{ path: 'record'}" class="mold-box"><span @click="record()">传记</span></router-link>
                    </el-breadcrumb>
                </el-col>
            </el-row>
        </el-container>
        <el-container>
            <router-view :mySqlData="mySqlData.slice((currentPage-1)*pageSize,currentPage*pageSize)" :total="total" :currentPage="currentPage" :pageSize="pageSize" v-on:currentPage="successz($event)"></router-view>
        </el-container>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'classify',
        components: {
            // HelloWorld
        },
        data(){
            return {
                activeIndex: '1',
                mySqlData:[],
                total:50,
                currentPage:1,
                pageSize:10,
            }
        },
        methods: {
            handleOpen() {
            },
            handleClose() {
            },
            successz(val){
                this.currentPage=val;
                this.pageSize=10;
                this.total=50;
                // alert(val)
            },
            action(){
                let data = {mold:'动作'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            war(){
                let data = {mold:'战争'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            science(){
                let data = {mold:'科幻'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            suspense(){
                let data = {mold:'悬疑'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            comedy(){
                let data = {mold:'喜剧'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            love(){
                let data = {mold:'爱情'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            inspiration(){
                let data = {mold:'剧情'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            animations(){
                let data = {mold:'动画'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            thriller(){
                let data = {mold:'惊悚'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            crime(){
                let data = {mold:'犯罪'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },
            record(){
                let data = {mold:'传记'};
                this.$axios.post("/api/classfiy",data)
                    .then((response) => {
                        // alert(response.data.data[1]['mname'])
                        this.mySqlData = response.data.data
                    })
                    .catch((error) => {
                        alert(error)
                    });
            },


        },
        mounted(){
            this.$axios.get('/api/information').then((data)=>{
                // alert(data.data.data[0].score);
                this.mySqlData = data.data.data
            }).catch((error)=>{
                alert(error)
            })
        },

    }
</script>
<style scoped>
    .classify-box{
        width: 100%;
        height: 100%;
        background-color: #FFF;
    }
    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
        /*line-height: 160px;*/
        padding: 0!important;
    }
    .el-aside {
        background-color: #ffffff;
        color: #333;
        text-align: center;
    }
    .el-menu{
        border: none;
    }
    .table-box{
        height: 20px;
        line-height: 20px;
        margin: 30px 0 20px 30px;
    }
    .mold-box:hover{
        color: #409EFF;
        cursor: pointer;
    }
</style>
