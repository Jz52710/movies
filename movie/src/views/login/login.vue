<template>
    <div class="login-box">
        <div id="title">
            <p class="logo">
                iMovies
                <span>爱生活 爱电影</span>
            </p>
        </div>
        <div id="oneWord">
            <p>Is life always this hard, or is it just when you're a kid ?</p>
            <p>Always like this.</p>
            <p>From Léon</p>
        </div>
        <div class="login-right">
            <p>用户登录</p>
            <el-form :model="ruleForm" :rules="rules" status-icon ref="ruleForm">

                <el-form-item prop="username">
                    <el-input placeholder="请输入用户名" clearable v-model="ruleForm.username" style="width: 284px;"></el-input>
                </el-form-item>

                <el-form-item prop="password">
                    <el-input placeholder="请输入密码" clearable v-model="ruleForm.password" type="password" style="width: 284px"></el-input>
                </el-form-item>

                <el-button type="primary" style="width:284px" @click="onSubmit('ruleForm')">登录</el-button>

            </el-form>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'login',
        components: {
            // HelloWorld
        },
        data(){
            return {
                ruleForm:{
                    username:'',
                    password:''
                },
                rules:{
                    username:[
                        { required: true, message: '请输入用户名',trigger:'blur'},
                        { min: 2, max: 20, message: '名字太长，请重新输入', trigger: 'blur' }
                    ],
                    password:[
                        { required: true, message: '请输入密码',trigger:'blur'},
                        { min: 6, message: '密码长度在6位以上', trigger: 'blur' }
                    ]
                }
            }
        },
        methods:{
            onSubmit(formName){
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$message({
                            message: '登录成功',
                            type: 'success',
                        });
                        this.$router.push({name:"index"});
                    } else {
                        this.$message.error('登录失败');
                        return false;
                    }
                });
            }
        },
    }
</script>
<style>
    .login-box{
        width: 100%;
        height: 100%;
        background: url("../../assets/bj.jpg") no-repeat;
        background-size: 100% 100%;
    }
    /*字*/
    #title {
        position: absolute;
        left: 8%;
        top: 5%;
    }
    #title span {
        padding-left: 20px;
        font-family: YouYuan;
        font-size: 0.2em;
    }
    #oneWord {
        position: absolute;
        top: 35%;
        left: 10%;
        width: 500px;
    }
    #oneWord p {
        font-size: 1em;
        font-family: "Lucida Handwriting",Arial;
    }
    #oneWord p + p {
        padding-left: 60%;
        padding-top: 5px;
    }
    #oneWord p + p + p {
        padding-left: 80%;
    }
    .logo {
        font-size: 5em;
        font-family: Axure "Axure Handwriting";
        font-weight: bold;
    }
    /*    登录*/
    .login-right{
        width: 310px;
        height: 230px;
        float: right;
        padding: 0 13px;
        box-sizing: border-box;
        position: absolute;
        right: 400px;
        top: 100px;
    }
    .login-right p{
        width: 284px;
        height: 40px;
        color: #33475F;
        font-size: 16px;
        line-height: 40px;
        text-align: left;
        margin: 0 auto;
    }
</style>
