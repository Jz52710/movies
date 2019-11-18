<template>
    <div class="classify-box">
        <el-container>
            <el-aside width="200px">电影分类</el-aside>
            <el-container>
                <el-main>对应影片</el-main>
            </el-container>
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
            handleSelect() {
            }
        }
    }
</script>
<style scoped>
    .classify-box{
        width: 100%;
        height: 100%;
    }
    .el-aside {
        background-color: #D3DCE6;
        color: #333;
        text-align: center;
        line-height: 200px;
    }

    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
        line-height: 160px;
        padding: 0!important;
    }
</style>
