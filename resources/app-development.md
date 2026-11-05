# App Development Resources

A free, practical path into mobile and cross-platform application development. Choose one platform path first, learn its language and UI model, then build, test, and release a small app.

> All linked documentation is free to access. App store accounts, developer programs, and some tooling may have fees; verify the current terms with Apple or Google before publishing. DevSphere does not sell courses or guarantee app-store approval.

## Choose your path

| Path | Language | Best when | Start here |
| --- | --- | --- | --- |
| **Native Android** | Kotlin | You want Android platform depth, Compose, and Google Play | [Android get started](https://developer.android.com/get-started), [Kotlin documentation](https://kotlinlang.org/docs/home.html) |
| **Native iOS** | Swift | You want Apple platform depth, SwiftUI, and the App Store | [Swift documentation](https://www.swift.org/documentation/), [SwiftUI tutorials](https://developer.apple.com/tutorials/swiftui) |
| **Flutter** | Dart | You want one codebase for Android, iOS, web, and desktop | [Flutter documentation](https://docs.flutter.dev/), [Dart documentation](https://dart.dev/docs) |
| **React Native** | JavaScript or TypeScript | You already know React and want native mobile targets | [React Native documentation](https://reactnative.dev/docs/getting-started) |
| **Expo** | JavaScript or TypeScript | You want a managed React Native workflow and quick device testing | [Expo documentation](https://docs.expo.dev/) |

There is no universally best path. Pick the one that matches your existing skills, target devices, and willingness to learn platform-specific behavior.

## Begin with one complete app

A small app you finish teaches more than five abandoned starters. Start with a focused scope:

- One primary user.
- Three to five screens.
- One data source.
- One persistence or offline decision.
- One accessibility requirement.
- One release checklist.

Good first projects: habit tracker, reading list, expense logger, study timer, local weather viewer, or event checklist.

## Android

| Resource | Level | Notes |
| --- | --- | --- |
| [Android get started](https://developer.android.com/get-started) | Beginner | Official setup and fundamentals |
| [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) | Beginner | Official course using Kotlin and Compose |
| [Kotlin documentation](https://kotlinlang.org/docs/home.html) | Beginner–Advanced | Language reference and guides |
| [Android design](https://developer.android.com/design) | Intermediate | Material design and interaction guidance |
| [Android accessibility](https://developer.android.com/guide/topics/ui/accessibility) | Intermediate | Accessible Android interfaces |
| [Android testing](https://developer.android.com/training/testing) | Intermediate | Unit, UI, and integration testing |
| [App versioning](https://developer.android.com/studio/publish/versioning) | Intermediate | Version codes, releases, and updates |
| [Publishing overview](https://developer.android.com/studio/publish) | Intermediate | Prepare and publish an Android app |

**Practice:** build a two-screen app with a list, a detail view, local persistence, a loading state, and an empty state. Test with large text and a screen reader.

## iOS

| Resource | Level | Notes |
| --- | --- | --- |
| [Swift documentation](https://www.swift.org/documentation/) | Beginner–Advanced | Official Swift language resources |
| [SwiftUI tutorials](https://developer.apple.com/tutorials/swiftui) | Beginner | Build interfaces with Apple's declarative framework |
| [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) | Intermediate | Apple platform design guidance |
| [Apple accessibility](https://developer.apple.com/documentation/accessibility) | Intermediate | Accessibility APIs and guidance |
| [XCTest](https://developer.apple.com/documentation/xctest) | Intermediate | Apple's testing framework |
| [App Store submission](https://developer.apple.com/app-store/submitting/) | Intermediate | Submission and review requirements |
| [App Store](https://developer.apple.com/app-store/) | All | Distribution platform and developer resources |

**Practice:** build a SwiftUI app with navigation, a form, validation, local persistence, and a clear error state. Test with Dynamic Type and VoiceOver.

## Flutter

| Resource | Level | Notes |
| --- | --- | --- |
| [Flutter documentation](https://docs.flutter.dev/) | Beginner–Advanced | Official guides and reference |
| [Flutter learning pathway](https://docs.flutter.dev/learn/pathway) | Beginner | Structured learning route |
| [Dart documentation](https://dart.dev/docs) | Beginner–Advanced | Language and API reference |
| [State management overview](https://docs.flutter.dev/data-and-backend/state-mgmt/intro) | Intermediate | Compare approaches before choosing one |
| [Flutter testing](https://docs.flutter.dev/testing) | Intermediate | Unit and widget testing |
| [Android deployment](https://docs.flutter.dev/deployment/android) | Intermediate | Build and release for Android |
| [iOS deployment](https://docs.flutter.dev/deployment/ios) | Intermediate | Build and release for iOS |

**Practice:** build an app with a list, detail screen, local storage, form validation, and two themes. Add a widget test for a critical interaction and test on both a small and a large screen.

## React Native and Expo

| Resource | Level | Notes |
| --- | --- | --- |
| [React Native documentation](https://reactnative.dev/docs/getting-started) | Beginner–Advanced | Official framework documentation |
| [React Native tutorial](https://reactnative.dev/docs/tutorial) | Beginner | Build a first native app |
| [Environment setup](https://reactnative.dev/docs/environment-setup) | Beginner | Choose Expo or a native toolchain |
| [React Native testing](https://reactnative.dev/docs/testing-overview) | Intermediate | Testing approaches and tools |
| [Expo documentation](https://docs.expo.dev/) | Beginner–Advanced | Managed workflow, build service, and APIs |
| [Expo tutorial](https://docs.expo.dev/tutorial/introduction/) | Beginner | Build and run a first Expo app |
| [Expo unit testing](https://docs.expo.dev/develop/unit-testing/) | Intermediate | Testing Expo applications |
| [Expo build introduction](https://docs.expo.dev/build/introduction/) | Intermediate | Build and distribution concepts |

**Practice:** build an app that fetches data, caches it locally, handles offline mode, and shows a useful error message. Test with the device's font-size settings enabled.

## Shared mobile concepts

### State and data

- Separate **server state** from **UI state**.
- Decide early whether the app is offline-first, online-only, or a hybrid.
- Model loading, empty, error, stale, and success states explicitly.
- Do not store secrets in client code or local storage.
- Treat the device as untrusted when designing APIs.

### Accessibility

- Support large text and screen readers.
- Keep touch targets large enough.
- Provide labels for icons and controls.
- Do not rely on color alone.
- Test with reduced motion and high contrast where supported.
- Check both portrait and landscape layouts.

### Privacy and permissions

Ask for a permission only when the user reaches a feature that needs it. Explain why it is needed, what happens if it is denied, and how the user can revoke it.

### Release quality

- Version builds consistently.
- Test upgrades, not only fresh installs.
- Prepare screenshots, descriptions, and privacy disclosures.
- Use staged rollouts where available.
- Have a rollback or hotfix plan.
- Monitor crashes and startup failures.

## Milestones

- [ ] I can build and run a starter app on a device or emulator.
- [ ] I can explain the platform's navigation and lifecycle model.
- [ ] I can handle loading, empty, error, and offline states.
- [ ] I can test one critical path on more than one screen size.
- [ ] I can describe the data my app collects and why.
- [ ] I can produce a release build and follow the store checklist.

## Avoid

- Choosing a framework before understanding the product.
- Building five screens before one screen works.
- Ignoring offline behavior until after launch.
- Hard-coding API keys in the mobile client.
- Requesting every permission at startup.
- Publishing without a privacy explanation.
- Assuming an emulator is the same as a real device.
- Treating app-store approval as guaranteed.

---

**Related:** [Mobile App Developer roadmap](learning-roadmaps.md#mobile-app-developer) · [Programming](programming.md) · [Web development](web-development.md) · [App Development discussions](https://github.com/Sumit-tech01/DevSphere-Community/discussions/categories/app-development)
