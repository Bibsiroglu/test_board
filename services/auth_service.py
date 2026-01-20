from services.supabase_client import supabase

class AuthService:
    @staticmethod
    def login_user(email, password):
        try:
            response = supabase.auth.sign_in_with_password({
                'email': email,
                'password': password
            })
            return response
        except Exception as e:
            raise e
        
    @staticmethod
    def logout_user():
        return supabase.auth.sign_out()
    
    @staticmethod
    def get_current_user():
        session = supabase.auth.get_session()
        if session:
            return session.user
        return None