<template>
    <div class="classify-box">
        <el-container>
            <el-row :span="24" style="display: flex">
                <el-col :span="24">
                    <el-breadcrumb separator="|" class="table-box">
                        <el-breadcrumb-item :to="{ path: 'action'} ">动作</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'war'}">战争</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'science'}">科幻</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'suspense'}">悬疑</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'comedy'}">喜剧</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'love'}">爱情</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'inspiration'}">剧情</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'animation'}">动画</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'thriller'}">惊悚</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'crime'}">犯罪</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: 'record'}">传记</el-breadcrumb-item>
                        <el-breadcrumb-item></el-breadcrumb-item>
                    </el-breadcrumb>
                </el-col>
            </el-row>
        </el-container>
        <el-container>
            <router-view></router-view>
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
                activeIndex: '1'
            }
        },
        methods: {
            handleOpen() {
            },
            handleClose() {
            },
        }
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
</style>
