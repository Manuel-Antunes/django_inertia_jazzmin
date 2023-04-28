import { InertiaProgress } from "@inertiajs/progress";
import { createInertiaApp } from "@inertiajs/react";
import axios from "axios";
import React from 'react';
import { createRoot } from 'react-dom/client';

export function resolvePageComponent(name: string, pages: any) {
  for (const path in pages) {
    if (path.endsWith(`${name.replace(".", "/")}.tsx`)) {
      return typeof pages[path] === "function" ? pages[path]() : pages[path];
    }
  }

  throw new Error(`Page not found: ${name}`);
}

document.addEventListener("DOMContentLoaded", () => {
  const csrfToken = (document.querySelector("meta[name=csrf-token]") as any)
    ?.content;
  axios.defaults.headers.common["X-CSRF-Token"] = csrfToken;

  InertiaProgress.init();

  createInertiaApp({
    resolve: name => {
      return resolvePageComponent(
        name,
        import.meta.glob("./Pages/**/*.tsx")
      );
    },
    setup({ el, App, props }) {
      createRoot(el).render(<App {...props} /> as React.ReactNode);
    },
  });
});
