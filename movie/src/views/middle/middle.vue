<template>
    <div class="index-box">
        <el-container>
            <el-main style="padding: 0!important;">
                <el-header>
                    <Header></Header>
                </el-header>
                <el-row style="width: 860px;margin: 0 auto">
                    <router-view></router-view>
                </el-row>
                <el-footer>
                    <el-row :span="24" style="font-size: 12px">
                        <span style="margin-right: 20px">Copyright © 2011-2018</span>
                        <span style="margin-right: 20px">
                            <a href="/" style="text-decoration: none;color: #cccccc">爱电影</a>
                        </span>
                        <span style="margin-right: 10px">京ICP备14003808号-5</span>
                        <span class="tu-box">
                            <img src="../../assets/ba-icon.png" alt="">
                            <span>京公网安备11010102002904号</span>
                        </span>
                    </el-row>
                </el-footer>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'
    import Header from '@/components/header/header.vue'

    export default {
        name: 'index',
        components: {
            // HelloWorld
            Header
        },
        data(){
            return {
                mysqlData:[],
                total:100,
                currentPage:1,
                pageSize:10,
            }
        },
        methods: {
            handleSelect() {
            },
            successz(val){
                this.currentPage=val;
                this.pageSize=10;
                this.total=100;
            }
        },
        mounted(){
            // let data = {'mold':'动作'};
            // this.$axios.post('/api/classfiy',data).then((data)=>{
            //     // alert(data.data.data[0].score);
            //     this.mysqlData = data.data.data
            // }).catch((error)=>{
            //     alert(error)
            // })
        },
    }
</script>
<style scoped>
    .index-box{
        width: 100%;
        height: 100%;
    }
    .el-container{
        width: 100%;
        height: 100%;
        /*background: #555;*/
    }
    .el-header{
        background-color: rgb(249, 249, 249);
        box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 4px;
        opacity: 0.97;
        color: #333;
        text-align: center;
        line-height: 60px;
        padding: 0 24px!important;
        /*position: fixed;*/
        z-index: 10;
        width: 100%;
    }
    .el-main {
        background-color: #F1F1F1;
        color: #333;
        text-align: center;
        /*line-height: 160px;*/
        /*padding: 0 24px!important;*/
    }
    .left-box{
        font-weight: 600;
        font-size: 24px;
    }
    .el-footer {
        background-color: #222222;
        color: #cccccc;
        text-align: center;
        line-height: 60px;
        height: 60px!important;
    }
    .zfx-box{
        width: 272px;
        height: 182px;
        margin: 30px 0 0 30px;
    }
    .war-box{
        width: 100%;
        height: 100%;
        background: #3498DB;
        position: relative;
        cursor: pointer;
        overflow: hidden;
        display: block;
    }
    .war-box span{
        position: absolute;
        right: 10px;
        top: 0;
        bottom: 0;
        margin: auto 0;
        font-size: 26px;
        color: white;
        line-height: 182px;
    }
    .war-box img{
        width: 100%;
        height: 100%;
        z-index: 10;
        position: absolute;
        top: 0;
        left: 0;
    }
    .ho-box{
        width: 100%;
        height: 100%;
        position: absolute;
        transition: all ease .4s;
    }
    .war-box:hover .ho-box{
        transform: translateX(-40px);
    }
    .name-box{
        position: absolute;
        z-index: 20;
        left: 0;
        top: 0;
        right: 0;
        bottom: 0;
        margin: auto;
    }
</style>
