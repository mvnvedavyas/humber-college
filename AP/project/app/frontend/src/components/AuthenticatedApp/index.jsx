import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Landing } from "../Landing";

function AuthenticatedApp() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
      </Routes>
    </BrowserRouter>
  );
}

export { AuthenticatedApp };
