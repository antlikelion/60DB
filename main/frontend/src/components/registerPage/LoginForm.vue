<template>
	<div class="formContainer">
		<div class="logoContainer">
			<img class="logo" src="../../assets/login_logo2.png" />
		</div>
		<form class="login-box">
			<p>아이디</p>
			<input
				type="text"
				@keyup.enter="login({ username, password })"
				v-model="username"
				name="username"
				label="ID를 입력하세요"
			/>
			<p>비밀번호</p>
			<input
				type="password"
				v-model="password"
				@keyup.enter="login({ username, password })"
				name="userpassword"
				label="비밀번호를 입력하세요"
			/>
			<br />
		</form>
		<div class="login-btn">
			<input
				type="submit"
				class="button"
				name="submit"
				@click="login({ username, password })"
				value="로그인"
			/>
			<input type="submit" class="button2" name="submit" @click="start" value="바로시작" />
			<div class="login-btn-txt">
				<a>아이디/비밀번호 찾기 |</a>
				<a class="bold">
					<router-link :to="{ name: 'signup' }">&nbsp;&nbsp;회원가입</router-link>
				</a>
			</div>
		</div>
	</div>
</template>
<script>
import { mapState, mapActions } from 'vuex';
export default {
	data() {
		return {
			username: null,
			password: null,
		};
	},
	computed: {
		...mapState(['isLogin', 'isLoginError']),
	},
	methods: {
		...mapActions(['login', 'start', 'resetRandomUser']),
	},
};
</script>
<style scoped>
/* logo */
.logoContainer {
	display: flex;
	justify-content: center;
	width: 100vw;
}
.logo {
	width: 350px;
	height: 200px;
}
/* form */
.formContainer {
	width: 100%;
	padding-top: 0.5rem;
	padding: auto;
}
.login-box {
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	width: 17rem;
	margin: auto;
}
.login-box p {
	margin: 0;
	padding: 0;
	font-size: 1rem;
	font-weight: 500;
}
.login-box input {
	width: 100%;
	margin-bottom: 1.5rem;
}
.login-box input[type='text'],
input[type='password'] {
	border: none;
	border-bottom: 1.5px solid #fff;
	background: transparent;
	outline: none;
	height: 35px;
}
.login-box input[type='password'] {
	font-family: '맑은고딕';
}
.login-btn {
	display: flex;
	flex-direction: column;
}
.button {
	background-color: white;
	border-radius: 10px;
	box-shadow: 0px 5px 5px 0px rgba(0, 0, 0, 0.308);
	outline-color: rgb(32, 114, 207);
	width: 15rem;
	height: 3rem;
	margin: auto;
	margin-top: 1rem;
	color: rgb(54, 54, 54);
	font-size: 1rem;
	font-weight: 700;
	/* transition: 0.5s; */
}
.button2 {
	background-color: rgb(255, 182, 47);
	border-radius: 10px;
	box-shadow: 0px 5px 5px 0px rgba(0, 0, 0, 0.308);
	outline-color: rgb(32, 114, 207);
	width: 15rem;
	height: 3rem;
	margin: auto;
	margin-top: 1rem;
	color: rgb(54, 54, 54);
	font-size: 1rem;
	font-weight: 700;
	/* transition: 0.5s; */
}
.button:hover {
	box-shadow: 5px 7px 10px 2px rgba(0, 0, 0, 0.308);
}
.button2:hover {
	box-shadow: 5px 7px 10px 2px rgba(0, 0, 0, 0.308);
}
.login-btn-txt {
	display: flex;
	justify-content: center;
	margin-top: 1.3rem;
	font-size: 0.9rem;
}
.bold {
	color: rgb(248, 215, 26);
	font-weight: 700;
}
a:visited {
	color: rgb(248, 215, 26);
}
</style>
