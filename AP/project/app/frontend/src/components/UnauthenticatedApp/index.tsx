import { useAuth } from "../../hooks/useAuth";
import LoginButton from "../LoginButton";
import "./styles.css";

function UnauthenticatedApp() {
  const { login } = useAuth();

  return (
    <div className="flex items-center justify-center w-full" style={{ height: '100vh' }}>
      <div className="flex flex-col items-center justify-center">
        <h2 className="mb-8 text-2xl text-white">
          Log in to join a chat room!
        </h2>

        <LoginButton action={login} />
      </div>
    </div>
  );
}

export { UnauthenticatedApp };
