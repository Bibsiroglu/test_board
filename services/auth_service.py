from core.database import db_client

class AuthService:
    @staticmethod
    def login_user(email, password):
        try:
            response = db_client.auth.sign_in_with_password({
                'email': email,
                'password': password
            })
            return response
        except Exception as e:
            raise e
        
    @staticmethod
    def logout_user():
        return db_client.auth.sign_out()
    
    @staticmethod
    def get_current_user():
        session = db_client.auth.get_session()
        if session:
            return session.user
        return None